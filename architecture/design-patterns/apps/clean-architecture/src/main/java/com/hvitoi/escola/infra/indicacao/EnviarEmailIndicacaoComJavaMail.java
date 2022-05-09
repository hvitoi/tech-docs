package com.hvitoi.escola.infra.indicacao;

import com.hvitoi.escola.aplicacao.indicacao.EnviarEmailIndicacao;
import com.hvitoi.escola.dominio.aluno.Aluno;

public class EnviarEmailIndicacaoComJavaMail implements EnviarEmailIndicacao {

	@Override
	public void enviarPara(Aluno indicado) {
		// logica de envio de email com a lib Java Mail
	}
}
