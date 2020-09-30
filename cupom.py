# coding: utf-8

class Loja:
  
  def __init__(self, nome_loja, logradouro, numero, complemento, bairro, 
               municipio, estado, cep, telefone, observacao, cnpj,
               inscricao_estadual):
    self.nome_loja = nome_loja
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual


def dados_loja_objeto(loja):

  if not loja.nome_loja:
    raise Exception ("O campo nome da loja é obrigatório")

  if not loja.logradouro:
    raise Exception ("O campo logradouro do endereço é obrigatório")

  if not loja.municipio:
    raise Exception ("O campo município do endereço é obrigatório")

  if not loja.estado:
    raise Exception ("O campo estado do endereço é obrigatório")

  if not loja.cnpj:
    raise Exception ("O campo CNPJ da loja é obrigatório")

  if not loja.inscricao_estadual:
    raise Exception ("O campo inscrição estadual da loja é obrigatório")

  _logradouro = loja.logradouro + ", "
  _numero = loja.numero and str(loja.numero) or "s/n"
  _complemento = loja.complemento and " " + loja.complemento or ""

  _bairro = loja.bairro and loja.bairro + " - " or ""
  _municipio = loja.municipio + " - "

  _cep = loja.cep and ("CEP:" + loja.cep) or ""
  _telefone = loja.telefone and ("Tel " + loja.telefone) or ""
  _telefone = (_telefone and _cep) and (" " + _telefone) or _telefone

  _observacao = loja.observacao and loja.observacao or ""

  _cnpj = "CNPJ: " + loja.cnpj
  _inscricao_estadual = "IE: " + loja.inscricao_estadual
  
  return \
f"""{loja.nome_loja}
{_logradouro}{_numero}{_complemento}
{_bairro}{_municipio}{loja.estado}
{_cep}{_telefone}
{_observacao}
{_cnpj}
{_inscricao_estadual}""" 
