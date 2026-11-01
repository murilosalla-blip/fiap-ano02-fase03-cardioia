"""Conferimos que exceções de apoio não autorizam retirar arquivos essenciais."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validar_organizacao import carregar_retirados, verificar_links_preservados
from fase1.verificar_preservacao import verificar


class PreservacaoApoioTest(unittest.TestCase):
    def setUp(self):
        base = Path(__file__).resolve().parents[2] / ".tools/tmp"
        base.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=base)
        self.root = Path(self.temp.name)
        assert self.root.resolve().is_relative_to(base.resolve())
        self.addCleanup(self.temp.cleanup)
        self.registros = self.root / "document/other/organizacao"
        self.registros.mkdir(parents=True)

    def gravar(self, retirado, original=None):
        self.registros.joinpath("higienizacao.json").write_text(json.dumps({
            "commit_recuperacao": "a" * 40, "retirados": [retirado] if retirado else [],
        }), encoding="utf-8")
        self.registros.joinpath("preservacao_fase1.json").write_text(json.dumps({
            "arquivos": [original] if original else [],
        }), encoding="utf-8")

    def item(self, caminho, categoria):
        return {"caminho": caminho, "categoria": categoria,
                "sha_git": "b" * 40, "sha256": "c" * 64, "sha256_lf": "c" * 64}

    def test_retirada_de_codigo_ou_dados_e_rejeitada(self):
        for caminho in ("src/fase3/python/consumidor_mqtt.py", "assets/fase1/dados/processed/base.csv",
                        "config/fase3/contratos/telemetria.schema.json", ".github/workflows/fase1-dados.yml"):
            with self.subTest(caminho=caminho):
                self.gravar(self.item(caminho, "aulas_pdf"))
                with self.assertRaisesRegex(AssertionError, "fora do escopo"):
                    carregar_retirados(self.root)

    def test_planejamento_interno_tem_excecao_individual(self):
        self.gravar(self.item("document/fase3/ROTEIRO_ENTREGA.md", "planejamento_interno"))
        self.assertEqual(1, len(carregar_retirados(self.root)))
        for caminho in ("document/fase3/CHECKLIST_ENUNCIADO.md", "document/fase3/CardioIA_Fase3_Relatorio_Edge.pdf",
                        "src/fase3/python/consumidor_mqtt.py", "assets/fase1/base.csv"):
            with self.subTest(caminho=caminho):
                self.gravar(self.item(caminho, "planejamento_interno"))
                with self.assertRaisesRegex(AssertionError, "fora do escopo"):
                    carregar_retirados(self.root)

    def test_alias_pode_mudar_de_documento_sem_desaparecer(self):
        alias = "https://github.com/murilosalla-blip/fiap-ano02-fase01-cap01-cardioia"
        video = "https://youtu.be/qoKjl6oeotY"
        self.root.joinpath("README.md").write_text(f"[Video]({video})", encoding="utf-8")
        self.registros.joinpath("README.md").write_text(f"[Alias]({alias})", encoding="utf-8")
        registro = {"urls": [alias, video], "realocados": {alias: "document/other/organizacao/README.md"}}
        self.registros.joinpath("links_externos_preservados.json").write_text(json.dumps(registro), encoding="utf-8")
        verificar_links_preservados(self.root)
        self.registros.joinpath("README.md").write_text("Alias removido", encoding="utf-8")
        with self.assertRaisesRegex(AssertionError, "Link externo removido"):
            verificar_links_preservados(self.root)

    def test_realocacao_nao_oculta_video_ou_material_essencial(self):
        for url in ("https://youtu.be/qoKjl6oeotY", "https://drive.google.com/drive/folders/material"):
            with self.subTest(url=url):
                registro = {"urls": [url], "realocados": {url: "document/other/organizacao/README.md"}}
                self.registros.joinpath("links_externos_preservados.json").write_text(json.dumps(registro), encoding="utf-8")
                with self.assertRaisesRegex(AssertionError, "não autorizada"):
                    verificar_links_preservados(self.root)

    def test_caminho_fora_do_projeto_e_rejeitado(self):
        self.gravar(self.item("../aula.pdf", "aulas_pdf"))
        with self.assertRaisesRegex(AssertionError, "Caminho"):
            carregar_retirados(self.root)

    def test_arquivo_essencial_ausente_nao_e_ignorado(self):
        self.gravar(None, {"preservado_em": "assets/fase1/base.csv", "imutavel": True, "sha_git": "b" * 40})
        with self.assertRaisesRegex(AssertionError, "Ausente"):
            verificar(self.root)

    def test_so_aula_original_pode_ficar_identificada_no_historico(self):
        p = "document/other/referencias/fase1/aulas/aula.pdf"
        item = self.item(p, "aulas_pdf")
        original = {"preservado_em": p, "imutavel": True, "sha_git": item["sha_git"]}
        self.gravar(item, original)
        self.assertEqual(len(carregar_retirados(self.root)), 1)
        self.assertEqual(verificar(self.root), 1)
        item["sha_git"] = "d" * 40
        self.gravar(item, original)
        with self.assertRaisesRegex(AssertionError, "indevida"):
            verificar(self.root)

    def test_excecao_nao_encobre_csv_do_manifesto_anterior(self):
        p = "assets/fase1/base.csv"
        self.gravar(self.item(p, "aulas_pdf"), {"preservado_em": p, "imutavel": True, "sha_git": "b" * 40})
        with self.assertRaisesRegex(AssertionError, "indevida"):
            verificar(self.root)

    def test_conteudo_essencial_alterado_e_rejeitado(self):
        p = "assets/fase1/base.csv"
        original = b"dado original\n"
        sha = hashlib.sha1(b"blob " + str(len(original)).encode() + b"\0" + original).hexdigest()
        self.gravar(None, {"preservado_em": p, "imutavel": True, "sha_git": sha})
        caminho = self.root / p
        caminho.parent.mkdir(parents=True)
        caminho.write_bytes(b"dado alterado\n")
        with self.assertRaisesRegex(AssertionError, "Alterado"):
            verificar(self.root)


if __name__ == "__main__":
    unittest.main()
