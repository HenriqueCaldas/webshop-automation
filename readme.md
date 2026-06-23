# Webshop Automation 🛒

Automação de testes para o site de e-commerce **[Demo Webshop](https://demowebshop.tricentis.com/)**, utilizando **Python, Selenium e Pytest**.

---

## 🚀 Tecnologias utilizadas
- [Python](https://www.python.org/) 3.x  
- [Selenium](https://www.selenium.dev/)  
- [Pytest](https://docs.pytest.org/)  
- [PyCharm](https://www.jetbrains.com/pycharm/)  

---

## 📂 Estrutura do projeto
webshop-automation/
│
├── DocumentTest/                  # Documentação de testes
│   └── Avaliação - Documentação de Testes - Luis Henrique.xlsx
│
├── pages/                         # Page Objects
│   ├── CartPage.py
│   ├── CompareProductsPage.py
│   ├── HomePage.py
│   ├── LoginPage.py
│   └── PDPPage.py
│
├── tests/                         # Casos de teste automatizados
│   ├── test_1.py
│   ├── test_validar_func_clearList.py
│   └── test_validar_preçoPDP_Carrinho.py
│
├── .gitignore
├── conftest.py
├── main.py
└── README.md


---

## 🧪 Casos de Teste Documentados

### CT-001 - Verificar funcionalidade *Clear list* na página de *Compare products*
- **Pré-condições:** Sistema disponível  
- **Procedimento:**  
  1. Acessar tela inicial da loja  
  2. Acessar vitrine de produtos  
  3. Acessar a PDP  
  4. Clicar em *Add to compare list*  
  5. Clicar em *Clear list*  
- **Resultado Esperado:**  
  - Mensagem *"You have no items to compare."* exibida  
  - Botão *Clear list* não visível  

---

### CT-002 - Consistência de preço entre PDP e Shopping Cart
- **Pré-condições:** Produto *14.1-inch Laptop* disponível  
- **Procedimento:**  
  1. Acessar tela inicial da loja  
  2. Acessar vitrine de notebooks  
  3. Clicar no produto *14.1-inch Laptop*  
  4. Acessar a PDP  
  5. Adicionar ao carrinho  
  6. Acessar o carrinho  
- **Resultado Esperado:**  
  - Valor capturado na PDP é o mesmo exibido no carrinho  

---

### CT-003 - Consistência no valor total e quantidade ao adicionar o mesmo produto duas vezes
- **Pré-condições:** Produto *14.1-inch Laptop* disponível  
- **Procedimento:**  
  1. Acessar tela inicial da loja  
  2. Acessar vitrine de notebooks  
  3. Clicar duas vezes em *Add to cart* no produto *14.1-inch Laptop*  
  4. Acessar o carrinho  
- **Resultado Esperado:**  
  - Valor unitário: 1590.00  
  - Valor total: 3180.00  
  - Quantidade: 2  
  - Subtotal no resumo: 3180.00  
  - Total no resumo: 3180.00  

---

## ⚙️ Configuração do ambiente
1. Clone o repositório:
   ```bash
   git clone git@github.com:HenriqueCaldas/webshop-automation.git
   cd webshop-automation

2. Crie e ative um ambiente virtual:
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Linux/Mac

3. Instale as dependências:
pip install -r requirements.txt

4. Executando os testes
pytest -v

5. Rodar um teste específico:
pytest tests/test_validar_func_clearList.py

📌 Observações
A documentação detalhada dos casos de teste está disponível em DocumentTest/Avaliação - Documentação de Testes - Luis Henrique.xlsx.

O ambiente de execução é Preprod.

O projeto segue boas práticas de automação com Page Objects e validações consistentes de preço e mensagens.

👨‍💻 Autor
Luis Henrique Beserra de Caldas


