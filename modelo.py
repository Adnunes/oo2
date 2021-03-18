class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} Likes'

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temp. - {self.likes} likes'


class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome.title()
        super().__init__(programas)



vingadores = Filme("vingadores - guerra infinitaa", 2018, 160)
atlanta = Serie("Atlanta", 2018, 2)
tdemp = Filme("todo mundo em pânico", 1999, 100)
demolidor = Serie("vingadores", 2016, 3)


vingadores.dar_like()
atlanta.dar_like()
tdemp.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()


filmes_e_series = [vingadores, atlanta,demolidor, tdemp]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f'Tamanho da playlist:  {len(playlist_fim_de_semana)}')
for programa in playlist_fim_de_semana:
   print(programa)

