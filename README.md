Repositório para resolução do <a href="Exercício 2 - I2C.pdf">exercício</a>. 

informaçõe gerais sobre as seguintes pastas descritas abaixo, para mais informações sobre
cada pasta, veja o README desta pasta. 

soluções testadas em uma raspberry py com uma distro linux como sistema operacional

# c_code

Nessa pasta tem um código em c(em conjunto do driver da bosch) que faz realizar  a medida
das 3 grandezas (Temperatura, Umidade e Pressão) a cada 1 segundo e registrar,
a cada 10 segundos, a média das amostras em um arquivo em formato CSV registrando data e hora de cada registro. 

# python_code

Nessa pasta tem um código em python3(em conjunto de um driver) que lê  3  grandezas  (Temperatura,  Umidade  e  Pressão)
do sensor BME280 e as apresente no display utilizando 2 casas decimais e sendo atualizadas a cada 1 segundo.
