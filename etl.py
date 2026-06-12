import pandas as pd
import os
import glob

def extrair_dados_e_consolidar(pasta:str) -> pd.DataFrame:
    #listar o que está na pasta e termina com .json
    #retorna uma lista com os arquivos .json na pasta
    arquivos_json = glob.glob(os.path.join(pasta,"*.json")) 

    #cria uma lista de data frames a partir dos arquivos lidos
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]

    #concatenar dfs, unir todos os dfs que tem o mesmo schema
    df_total = pd.concat(df_list,ignore_index=True)

    return df_total

def calcular_kpi_de_total_de_vendas(df:pd.DataFrame)->pd.DataFrame:
    #adicionar uma coluna vendas*quantidade pra obter o total
    df["Total"] = df["Quantidade"]*df["Venda"]
    return df

def salvar_dados(formato_saida, df):
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv('data/output.csv',index=False,encoding='utf-8')
        if formato == 'parquet':
            df.to_parquet('data/output.parquet')


#teste unitário
if __name__ == "__main__":
    pasta = 'data'
    formato_saida:list=["csv","parquet"]
    df=extrair_dados_e_consolidar(pasta)
    df_calculado = calcular_kpi_de_total_de_vendas(df)
    salvar_dados(formato_saida,df_calculado)