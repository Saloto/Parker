# -*- coding: utf-8 -*-
import scrapy
import re


class Parkerv1Spider(scrapy.Spider):
    name = 'Parkerv1'

    def start_requests(self):
        user = input("Digite o nome de usuário da pessoa alvo:")
        facebook = "https://pt-br.facebook.com/"
        sufixs = ["","/about/?ref=page_internal", "/videos/?ref=page_internal", "/posts/?ref=page_internal", "/events/?ref=page_internal", "/notes/?ref=page_internal", "/photos/?ref=page_internal", "/community/?ref=page_internal", "/ads/?ref=page_internal"]
        for sufix in sufixs:
            url = facebook + user + sufix
            #yield scrapy.Request(url=url, callback=self.parse)
            if re.search(r'about', url) is not None:
                yield scrapy.Request(url=url, callback=self.dados_about)
            '''elif re.search(r'videos', url) is not None:
                yield scrapy.Request(url=url, callback=self.dados_about)
            elif re.search(r'posts', url) is not None:
                yield scrapy.Request(url=url, callback=self.dados_about)
            elif re.search(r'events', url) is not None:
                yield scrapy.Request(url=url, callback=self.dados_about)
            elif re.search(r'notes', url) is not None:
                yield scrapy.Request(url=url, callback=self.dados_about)
            elif re.search(r'photos', url) is not None:
                yield scrapy.Request(url=url, callback=self.dados_about)
            elif re.search(r'community', url) is not None:
                yield scrapy.Request(url=url, callback=self.dados_about)
            elif re.search(r'ads', url) is not None:
                yield scrapy.Request(url=url, callback=self.dados_about)
            else:
                pass'''


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def dados_about(self, response):
        arquivo = open('/root/Desktop/compart/Parker/resultado.txt','a')
        arquivo.write("RELATÓRIO DE PÁGINA DO FACEBOOK")
        arquivo.write('\n\n')

        nome = response.xpath('//a[@class="_64-f"]/span/text()').extract()
        arquivo.write("O nome do usuário é: ")
        arquivo.write(str(nome))
        arquivo.write('\n')

        # list1 recebe Nasceu em..., Cidade Natal, Sobre, Biografia, Prêmios e Sobre mim
        list1 = response.xpath('//div[@class="_5aj7 _3-8j"]/div[@class="_4bl9"]/div[@class="_50f4"]/text()').extract()
        # Aqui separa só a data de nascimento
        try:
            nascimento = list1[0].split(" em")
            arquivo.write("Data de nascimento:")
            arquivo.write(str(nascimento[1]))
            arquivo.write('\n')
        except IndexError:
            arquivo.write('\n')
            pass

        #list2 recebe os textos de Cidade natal, Sobre e Sobre mim
        list2 = response.xpath('//div[@class="_5aj7 _3-8j"]/div[@class="_4bl9"]/div[@class="_3-8w"]/text()').extract()
        arquivo.write("Cidade Natal: ")
        arquivo.write(str(list2[0]))
        arquivo.write('\n')
        arquivo.write("Sobre: ")
        arquivo.write(str(list2[1]))
        arquivo.write('\n')
        arquivo.write("Sobre mim: ")
        arquivo.write(str(list2[2]))
        arquivo.write('\n')

        #só pra gerar um espaço no final
        arquivo.write('\n\n')

        arquivo.close()
