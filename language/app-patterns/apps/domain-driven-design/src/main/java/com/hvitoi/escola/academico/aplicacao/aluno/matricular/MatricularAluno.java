package com.hvitoi.escola.academico.aplicacao.aluno.matricular;

import com.hvitoi.escola.academico.dominio.aluno.Aluno;
import com.hvitoi.escola.academico.dominio.aluno.AlunoMatriculado;
import com.hvitoi.escola.academico.dominio.aluno.RepositorioDeAlunos;
import com.hvitoi.escola.shared.dominio.evento.PublicadorDeEventos;

public class MatricularAluno {

	private final RepositorioDeAlunos repositorio;
	private final PublicadorDeEventos publicador;

	// inversion of dependency
	public MatricularAluno(RepositorioDeAlunos repositorio, PublicadorDeEventos publicador) {
		this.repositorio = repositorio;
		this.publicador = publicador;
	}

	// COMMAND
	public void executa(MatricularAlunoDto dados) {
		Aluno novo = dados.criarAluno();
		repositorio.matricular(novo);

		AlunoMatriculado evento = new AlunoMatriculado(novo.getCpf());
		publicador.publicar(evento);
	}

}
