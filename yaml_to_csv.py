import yaml
import openpyxl
import csv


class ObjetoYaml:
    def __init__(self, arquivo_yaml):
        self.arquivo_yaml = arquivo_yaml
        self.__correcoes = arquivo_yaml["correcoes"]
        self.__respostas = arquivo_yaml["respostas"]

    @property
    def correcoes(self):
        return self.__correcoes

    @property
    def respostas(self):
        return self.__respostas

    def tarefa(self, tarefa):
        return self.__correcoes[tarefa]

    def retorna_avaliadores_de_uma_tarefa_dado_um_aluno(self, tarefa, aluno):
        return list(self.__correcoes[tarefa][aluno])

    def retorna_lista_tarefas(self):
        return list(self.__correcoes.keys())

    def retorna_lista_alunos_dada_uma_tarefa(self, tarefa):
        return list(self.__correcoes[tarefa].keys())

    def retorna_uma_avaliacao_da_tarefa_de_um_aluno(self, tarefa, aluno, avaliador):
        return self.__correcoes[tarefa][aluno][avaliador]

    def __str__(self):
        return str(self.yaml_data)


class YamlParaCSV:
    def __init__(self, arquivo_csv, objeto_yaml):
        self.arquivo_csv = arquivo_csv
        self.__instancia_yaml = objeto_yaml
        self.__tarefas = self.__instancia_yaml.retorna_lista_tarefas()

    def processa_yaml(self):
        with open(self.arquivo_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            cabecalho = [
                'Aluno',
                'Tarefa',
                'Avaliador',
                'Entregou',
                'Passou do Prazo',
                'Facilidade de Reproduzir',
                'Legibilidade',
                'Feedback Positivo',
                'Feedback Melhorar',
                'Rank',
                'Objetivo Primario',
                'Objetivo Secundario',
            ]

            writer.writerow(cabecalho)

            # Percorre os dados e escreve no arquivo CSV
            for tarefa in self.__tarefas:
                for aluno in self.__instancia_yaml.retorna_lista_alunos_dada_uma_tarefa(tarefa):
                    for avaliador in self.__instancia_yaml.retorna_avaliadores_de_uma_tarefa_dado_um_aluno(tarefa, aluno):
                        avaliacao = self.__instancia_yaml.retorna_uma_avaliacao_da_tarefa_de_um_aluno(
                            tarefa, aluno, avaliador)
                        tam_cabecalho_tirando_os_3_primeiros = len(cabecalho) - 3
                        if (avaliacao != 0):
                            dados = [
                                aluno,
                                tarefa,
                                avaliador,
                                *avaliacao.values(),
                            ]
                        else:
                            dados = [
                                aluno,
                                tarefa,
                                avaliador,
                                *['Não Avaliado']*tam_cabecalho_tirando_os_3_primeiros,
                            ]
                        writer.writerow(dados)
            csvfile.close()


def abre_yaml(nome):
    yaml_data = None
    with open(nome, "r") as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    return yaml_data

#yaml_data = abre_yaml('avaliacoes.yaml')

#obj_yaml = ObjetoYaml(yaml_data)
#obj_csv = YamlParaCSV('file.csv', obj_yaml)
#obj_csv.processa_yaml()


