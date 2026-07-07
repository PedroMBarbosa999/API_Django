# API_Django
API de um app mobile de administração de tarefas

Paso a paso:
1. preparação do ambiente
2. preparação de arquivos auxilares (urls.py, models, seriallazer e etc.)
3. criação dos endpoints simples (GET, POST, PUT e DELETE) do User (sempre que criado um endpoint eu aidcionei a url dele ao admtarefas/urls.py, tive que nesse ponto usar IA por conta de um erro que não sabia como resolver, mas pedi pra IA fazer um analise do codigo para tentar me ajudar a corrigir e entender o erro, a IA me sugeriu alguns ajuste e pedi que ela ajustasse para mim)
4. criação de um sistema de login (perguntei para IA qual o melhor para login POST, PUT ou GET e pedi pra ela melhorar a logica do codigo, ela manteve minha ideia inicial e melhorou ela)
5. criptografia dos dados atuais (perguntei para IA os melhores jeitos de fazer isso, ela deu o hash e a biblioteca de criptografia do Python, decidi por usar o PKBDF2 que já inserido no próprio Django)
6. criação do model de tasks para criar os campos da tarefa
7. preparação de arquivos auxiliares(serializer, urls e outros)
8. criação dos endpoints simples (GET, POST, PUT e DELETE)
9. criação de um endpoint que puxa a tarefa pelo user_id
10. configuração do CORS (pedi pra IA configurar, tive que fazer uma mudança no views por conta do login)

OBS: usei VS Code Stuido, ele vem com IA integrada que dá sugestões, mas não aceito as sugestões, a menos que seja algo que eu não saiba fazer, resolver ou para melhorias

bibliotecas:
Django
Django RestFramework
Django Serializer
Django PKBDF2
Django Simplejwt