# Explorando o Módulo `subprocess` do Python

O Python inclui o módulo `subprocess`, uma ferramenta poderosa para executar programas externos e capturar suas saídas diretamente em seus scripts. Essa funcionalidade pode ser usada para controlar programas no sistema, como por exemplo, interagir com o `git` ou executar scripts Python adicionais.

O módulo `subprocess` é útil quando se precisa combinar a funcionalidade de diferentes programas em um único fluxo de trabalho.

---

## **Usando `subprocess.run`**

O método subprocess.run é um dos mais versáteis do módulo, permitindo executar comandos com grande controle sobre sua execução. Ele fornece diversas opções para configurar como o processo externo será tratado. Por exemplo, é possível:

- Capturar Saídas: O argumento capture_output permite armazenar as saídas padrão (stdout) e de erro (stderr) do comando para uso posterior.
- Passar Entradas: O parâmetro input pode ser usado para fornecer dados ao programa por meio do stdin.
- Controlar Timeout: O argumento timeout ajuda a evitar que o programa externo fique em execução por tempo indeterminado, encerrando-o automaticamente após um período especificado.
- Gerenciar Erros: Com o parâmetro check, o Python pode lançar uma exceção automaticamente caso o comando retorne um código de erro.
- Redirecionar Fluxos: É possível redirecionar saídas ou entradas para arquivos ou outras fontes, integrando o programa externo ao fluxo de trabalho do script.

---

## **Conclusão**

O módulo `subprocess` no Python permite executar e controlar programas externos diretamente nos seus scripts. Com ele é possível:

- Capturar saídas e erros.
- Tratar exceções de execução.
- Configurar limites de tempo para processos.
- Passar entradas diretamente via stdin.

