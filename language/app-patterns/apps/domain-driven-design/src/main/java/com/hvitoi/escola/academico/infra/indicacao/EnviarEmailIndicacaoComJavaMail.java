package com.hvitoi.escola.academico.infra.indicacao;

import com.hvitoi.escola.academico.aplicacao.indicacao.EnviarEmailIndicacao;
import com.hvitoi.escola.academico.dominio.aluno.Aluno;

public class EnviarEmailIndicacaoComJavaMail implements EnviarEmailIndicacao {

	@Override
	public void enviarPara(Aluno indicado) {
		// logica de envio de email com a lib Java Mail
	}
}
