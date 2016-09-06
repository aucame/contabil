# -*- coding: utf-8 -*-
import subprocess, time, json

# Reescreve o método para uso no python2.6
if "check_output" not in dir( subprocess ): # duck punch it in!
    def f(*popenargs, **kwargs):
        if 'stdout' in kwargs:
            raise ValueError('stdout argument not allowed, it will be overridden.')
        process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
        output, unused_err = process.communicate()
        retcode = process.poll()
        if retcode:
            cmd = kwargs.get("args")
            if cmd is None:
                cmd = popenargs[0]
            raise subprocess.CalledProcessError(retcode, cmd)
        return output
    subprocess.check_output = f

class Prevision():
    def checkPrc(self, processo):
        #return subprocess.check_output('ps ax | grep prevision | grep -v grep | awk \'{print $1}\'',shell=True)
        return len((subprocess.check_output('ps ax | grep '+processo+' | grep -v grep | awk \'{print $1}\'',shell=True)).split('\n')) -1

    def countProcess(self, processo):
        retorno = {'Processo': processo, 'Execucoes': self.checkPrc(processo)}
        retorno = json.dumps(retorno, sort_keys = False, indent = 4)

        return retorno

    def executar(self, category_id):
        caminho = '/home/em_dourado/Documentos/Fontes/Abastecimento/Prevision/planejamentoabastecimento-previsionluiza/python/calculate/api/api/scripts/'
        retorno = {}

        if self.checkPrc('prevision'):
            retorno = {'status': 'ERRO', 'resumo': 'Ja existe um processo no servidor', 'descricao': 'Ja existe um processo em execucao no servidor!'}
        else:
            try:
                ret = subprocess.Popen(['python', caminho+'prevision.py', '{0}'.format(category_id)], close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                time.sleep(0.1)

                if not self.checkPrc('prevision'):
                    stdout_data = ret.communicate()
                    retorno = {'status': 'ERRO', 'resumo': 'Falha ao rodar alocacao', 'descricao': stdout_data}
                else:
                    retorno = {'status': 'SUCESSO', 'resumo': 'Linha ' + category_id + ' iniciada', 'descricao': 'Processo de alocacao iniciado com sucesso!'}
            except Exception as erro:
                print erro
                retorno = {'status': 'ERRO', 'resumo': 'Falha ao executar processo', 'descricao': 'Falha ao executar processo'}

        retorno = json.dumps(retorno, sort_keys = False, indent = 4)

        return retorno
