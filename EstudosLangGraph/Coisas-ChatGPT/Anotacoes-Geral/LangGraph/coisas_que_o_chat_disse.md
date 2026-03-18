# LangGraph

LLM -> Large Language Model

Exemplos {
    GPT-4
    Claude
    Gemini
}

Esses modelos consegue:
- responder perguntas
- escrever códigos
- resumir textos
- traduzir
- analisar dados textuais

------
#### Em Grafo temos

##### Node (Nodes/Vértices)
Um node é uma função

##### Edge (Arestas/Conexões)
Um edge é uma conexão entre nodes

-----

##### State

State (estado)
é o dicionário compartilhado entre nodes.
(cada node poder [ler e alterar])

-----

##### Um Grafo é definido como:
G = (V, E)  
Conjunto de Node e Edge, torna um Grafo  
V = conjunto de vértices (nodes)
E = conjunto de arestas (edges)

-----

##### O que é Workflow
**Workflow** são **fluxos de execução estruturados**  
onde cada etapa do processo é representada como  
um **nó de um grafo** e as conexões entre eles  
definem a **ordem em que as coisas acontecem**.

Em outras palavras...

Um workflow é o caminho que os dados percorrem dentro do grafo, passando por várias etapas até chegar ao resultado final.

Um workflow define:  
1- Quais etapas existem;  
2- Em que ordem elas acontecem;  
3- Como os dados passam entre elas.

-----

##### Diferença entre Workflow e Agent

Workflow tem um fluxo pré-definido.

Agente decide o que fazer. - Tem um fluxo dinâmico

-----

##### Diferença entre Workflow e Pipeline

Workflow tem um fluxo com decisões e caminhos diferentes

Pipeline tem um fluxo linear

-----

##### Opções de validação/código no node

- Regex
- Embedding Similarity
- LLM

-----

### Motivo para usar LangGraph

##### Um LLM sozinho não:
 - Não acessa banco de dados;
 - Não chama APIs;
 - Não executa códigos;
 - Não toma decisões complexas;
