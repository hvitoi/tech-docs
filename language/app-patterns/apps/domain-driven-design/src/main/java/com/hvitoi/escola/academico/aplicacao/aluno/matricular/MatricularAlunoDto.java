package com.hvitoi.escola.academico.aplicacao.aluno.matricular;

import com.hvitoi.escola.academico.dominio.aluno.Aluno;
import com.hvitoi.escola.academico.dominio.aluno.Email;
import com.hvitoi.escola.shared.dominio.CPF;

public class MatricularAlunoDto {

	private String nomeAluno;
	private String cpfAluno;
	private String emailAluno;

	public MatricularAlunoDto(String nomeAluno, String cpfAluno, String emailAluno) {
		this.nomeAluno = nomeAluno;
		this.cpfAluno = cpfAluno;
		this.emailAluno = emailAluno;
	}

	public Aluno criarAluno() {
		return new Aluno(new CPF(cpfAluno), nomeAluno, new Email(emailAluno));
	}

}
