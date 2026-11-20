"""Testes estruturais do princípio AXI 2.4.1, não ensaios com LLMs."""
import unittest
from pathlib import Path
import xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
S=(R/"skill/axipesquisa/SKILL.md").read_text("utf-8")
M=(R/"skill/axipesquisa/references/INVESTIGACAO-RECURSIVA.md").read_text("utf-8")
class RecursaoAXI(unittest.TestCase):
    def test_oito_movimentos(self):
        for t in (S,M):
            for n in ("Identificar o todo","Identificar as partes","Identificar a função do todo",
                      "Identificar a função de cada parte","Expandir o todo","Expandir cada parte",
                      "Integrar o todo","Integrar cada parte"):
                self.assertIn(n,t)
            self.assertIn("partes → todo",t)
            self.assertIn("todo → partes",t)
    def test_recursao_e_visuais(self):
        self.assertIn("todo-pai",S)
        self.assertIn("Critério de parada",M)
        self.assertIn("Markmap da A não substitui Mermaid da I",S)
        image=R/"docs/figuras/axi-recursividade-v2.4.1.svg"
        self.assertEqual(ET.parse(image).getroot().tag,"{http://www.w3.org/2000/svg}svg")
        self.assertIn("docs/figuras/axi-recursividade-v2.4.1.svg",(R/"README.md").read_text("utf-8"))
if __name__=="__main__":unittest.main()
