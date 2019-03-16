# Stop - The Game (em andamento)
![stop](https://raw.githubusercontent.com/GeovaneNarciso/POO_ADS2018.2_MOD2/master/Atv_X_Final_Java/passos/Stop-logo.jpg)

O Stop-The Game é um jogo de stop(adedonha), onde os jogadores reunidos em uma sala devem à cada rodada da partida, escrever palavras baseadas em categorias, e que tenham a letra inicial igual a letra sorteada da rodada.
Ao término de cada rodada os jogadores avaliam as palavras e são distribuídos os pontos para cada jogador, ao final da partida o jogador com mais pontos é o campeão.

## Classes Modelo
- **Jogador**
  - Atributos
    - id;
    - nome;
    - email;
    - senha;
    - pontos;
    - resposta;
    - pontuação total
  - Métodos
    - getters e setters.
- **Sala**
  - Atributos
    - id;
    -  maxRodadas;
    -  maxJogadores;
    - dono;
    - lista de jogadores;
    - lista de categorias;
    - partida;
  - Métodos
    - adicionar jogador;
    - getters e setters.
- **Partida**
  - Atributos
    - lista de jogadores;
    - lista de pontuação.
    - rodada
  - Métodos
    - getters e setters.
- **Pontuação**
  - Atributos
    - id do jogador;
    - pontos.
  - Métodos
    - getters e setters.
- **Rodada**
  - Atributos
    - tempo;
    - letra sorteada;
    - ponto parcial.
  - Métodos
    - getters e setters.
## Relacionamentos
Um jogador pode entrar em uma sala (que pode ter vários jogadores), a sala tem uma ou várias partidas (que só pode estar em uma sala), cada partida contém uma ou mais rodadas (que só pode estar em uma partida) e possui uma pontuação (que deve ter uma partida ou rodada). O jogador possui uma pontuação (que só pode estar em um jogador).
## Persistência de dados
Pretende-se usar o Firebase.
## Diagrama de Classe simplificado
![diagrama de classe simplificado](https://raw.githubusercontent.com/GeovaneNarciso/POO_ADS2018.2_MOD2/master/Atv_X_Final_Java/passos/PassoBC.jpg)
## Funcionalidades
- Cadastrar novo usuário ou entrar em uma conta já existente;
- Criar sala ou entrar em sala já existente (através do código da sala);
- Informar palavras (respostas) e avaliar as palavras dos outros jogadores.
## Requisitos e Restrições
- Framework para linguagem de programação Java;
## Storyboard de navegação
- Storyboard baseado em uma aplicação Android.

![storyboard](https://raw.githubusercontent.com/GeovaneNarciso/POO_ADS2018.2_MOD2/master/Atv_X_Final_Java/passos/PassoD.jpg)

## Meta
Geovane Narciso da Silva - geovane.ns@msn.com
https://github.com/GeovaneNarciso/POO_ADS2018.2_MOD2/tree/master/Atv_X_Final_Java

