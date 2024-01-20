from src.server import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# def decorator(funcao):
#     def funcao_superior(*arg, **kwargs):
#         print('Ola Mundo')
#         print(arg)
#         print(kwargs)
#         funcao(*arg)

#     return funcao_superior

# class minha_class:

#     @decorator
#     def metodo(self, num):
#         print('Estou na minha classe') 

# cl = minha_class()
# cl.metodo(4)       