package com.hvitoi.escola.aplicacao.aluno.matricular;

import com.hvitoi.escola.dominio.aluno.Aluno;
import com.hvitoi.escola.dominio.aluno.RepositorioDeAlunos;

public class MatricularAluno {

	private final RepositorioDeAlunos repositorio;

	public MatricularAluno(RepositorioDeAlunos repositorio) {
		this.repositorio = repositorio;
	}

	// Design Pattern "COMMAND"
	public void executa(MatricularAlunoDto dados) {
		Aluno novo = dados.criarAluno();
		repositorio.matricular(novo);
	}

}
