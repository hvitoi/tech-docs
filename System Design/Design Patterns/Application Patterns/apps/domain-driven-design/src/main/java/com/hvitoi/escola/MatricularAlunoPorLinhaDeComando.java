package com.hvitoi.escola;

// acessa multiplos contextos
import com.hvitoi.escola.academico.aplicacao.aluno.matricular.MatricularAluno;
import com.hvitoi.escola.academico.aplicacao.aluno.matricular.MatricularAlunoDto;
import com.hvitoi.escola.academico.dominio.aluno.LogDeAlunoMatriculado;
import com.hvitoi.escola.academico.infra.aluno.RepositorioDeAlunosEmMemoria;
import com.hvitoi.escola.gamificacao.aplicacao.GeraSeloAlunoNovato;
import com.hvitoi.escola.gamificacao.infra.selo.RepositorioDeSelosEmMemoria;
import com.hvitoi.escola.shared.dominio.evento.PublicadorDeEventos;

public class MatricularAlunoPorLinhaDeComando {

	public static void main(String[] args) {
		String nome = "Fulano da Silva";
		String cpf = "123.456.789-00";
		String email = "fulano@email.com";
		MatricularAlunoDto dto = new MatricularAlunoDto(nome, cpf, email);

		// Cria publicador de eventos e adiciona publicadores
		PublicadorDeEventos publicador = new PublicadorDeEventos();
		publicador.adicionar(new LogDeAlunoMatriculado());
		publicador.adicionar(new GeraSeloAlunoNovato(new RepositorioDeSelosEmMemoria()));

		// Objeto que matricula alunos
		MatricularAluno matricular = new MatricularAluno(new RepositorioDeAlunosEmMemoria(), publicador);
		matricular.executa(dto);
	}

}
