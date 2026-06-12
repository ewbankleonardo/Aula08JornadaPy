from etl import pipeline_kpi_vendas_consolidado

pasta = 'data'
formato_saida = ["csv"]

pipeline_kpi_vendas_consolidado(pasta,formato_saida)