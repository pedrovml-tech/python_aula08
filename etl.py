import pandas as pd
import glob
import os



# Ler todos os arquivos JSON de um diretório

def extrair_dados_json(diretorio_json: str) -> pd.DataFrame:
    """
    Função que lê todos os arquivos JSON de um diretório e retorna um Dataframe.
    """

    arquivos_diretorio = glob.glob(os.path.join(diretorio_json, '*.json'))
    df_list = [pd.read_json(path_or_buf=arquivo) for arquivo in arquivos_diretorio]
    df_concatenado = pd.concat(df_list, ignore_index=True)

    return df_concatenado


def calcular_valor_total_vendas(df_vendas : pd.DataFrame) -> pd.DataFrame:
    """
    Função que calcula o valor total da(s) venda(s)
    """

    df_vendas['Total'] = df_vendas['Quantidade'] * df_vendas['Venda']

    return df_vendas


def exportar_vendas_calculadas(formato_saida: list[str], df_calculado : pd.DataFrame) -> None:
    """
    Função que exporta os dados das vendas para o(s) formato(s) desejado(s)
    """

    if 'csv' in formato_saida:
        df_calculado.to_csv('resultado.csv', index=False)
    
    if 'parquet' in formato_saida:
        df_calculado.to_parquet('resultado.parquet', index=False) 


if __name__ == '__main__':
    pasta_json = 'data'
    df_base = extrair_dados_json(diretorio_json=pasta_json)
    df_vendas = calcular_valor_total_vendas(df_vendas=df_base)
    exportar_vendas_calculadas(formato_saida=['csv','parquet'], df_calculado=df_vendas)