import unittest
import os
from yaml_to_csv import ObjetoYaml, YamlParaCSV, abre_yaml

class TestMyApp(unittest.TestCase):
    def test_abre_corretamente_arquivo_yaml(self):
        result = abre_yaml('avaliacoes.yaml')
        self.assertTrue(type(result) == dict)
    
    def test_cria_objeto_yaml(self):
        result = ObjetoYaml(abre_yaml('avaliacoes.yaml'))
        self.assertTrue(type(result) == ObjetoYaml)
    
    def test_objeto_yaml_deve_retornar_tarefas(self):
        result = ObjetoYaml(abre_yaml('avaliacoes.yaml'))
        self.assertTrue(type(result.retorna_lista_tarefas()) == list)
    
    def test_objeto_yaml_deve_retornar_pelo_menos_uma_tarefa_valida(self):
        result = ObjetoYaml(abre_yaml('avaliacoes.yaml'))
        self.assertEqual(result.retorna_lista_tarefas()[0], 'life-python')
    
    def test_objeto_yaml_deve_retornar_dict_de_correcoes(self):
        result = ObjetoYaml(abre_yaml('avaliacoes.yaml'))
        self.assertTrue(type(result.correcoes) == dict)

    def test_objeto_yaml_deve_retornar_lista_de_respostas(self):
        result = ObjetoYaml(abre_yaml('avaliacoes.yaml'))
        self.assertTrue(type(result.respostas) == list)
    
    def test_objeto_yaml_deve_retornar_lista_de_alunos_dada_uma_tarefa(self):
        result = ObjetoYaml(abre_yaml('avaliacoes.yaml'))
        self.assertTrue(type(result.retorna_lista_alunos_dada_uma_tarefa('life-python')) == list)
    
    def test_objeto_yaml_deve_retornar_lista_de_avaliadores_de_uma_tarefa_dado_um_aluno(self):
        result = ObjetoYaml(abre_yaml('avaliacoes.yaml'))
        self.assertTrue(type(result.retorna_avaliadores_de_uma_tarefa_dado_um_aluno('life-python', 'ana.col')) == list)
    
    def test_objeto_yaml_deve_retornar_lista_de_tarefas(self):
        result = ObjetoYaml(abre_yaml('avaliacoes.yaml'))
        self.assertTrue(type(result.retorna_lista_tarefas()) == list)
    
    def test_objeto_yaml_deve_retornar_uma_avaliacao_de_uma_tarefa_de_um_aluno(self):
        result = ObjetoYaml(abre_yaml('avaliacoes.yaml'))
        self.assertTrue(type(result.retorna_uma_avaliacao_da_tarefa_de_um_aluno('life-python', 'ana.col', 'bruna.tula')) == dict)
    
    def test_processa_csv_corretamente(self):
        obj_yaml = ObjetoYaml(abre_yaml('avaliacoes.yaml'))
        arquivo_nome = 'file.csv'
        resultado = YamlParaCSV(arquivo_nome,obj_yaml)
        resultado.processa_yaml()
        self.assertTrue(os.path.exists(arquivo_nome))
    

if __name__ == '__main__':
    unittest.main()
