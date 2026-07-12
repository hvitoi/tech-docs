package com.hvitoi.escola.academico.aplicacao.aluno.matricular;

import static org.junit.jupiter.api.Assertions.assertEquals;

import com.hvitoi.escola.academico.dominio.aluno.Aluno;
import com.hvitoi.escola.academico.infra.aluno.RepositorioDeAlunosEmMemoria;
import com.hvitoi.escola.shared.dominio.CPF;
import com.hvitoi.escola.shared.dominio.evento.PublicadorDeEventos;

import org.junit.jupiter.api.Test;

class MatricularAlunoTest {

	@Test
	void alunoDeveriaSerPersistido() {
		// MOCK -> Mockito
		RepositorioDeAlunosEmMemoria repositorio = new RepositorioDeAlunosEmMemoria();

		MatricularAluno useCase = new MatricularAluno(repositorio, new PublicadorDeEventos());

		MatricularAlunoDto dados = new MatricularAlunoDto("Fulano", "123.456.789-00", "fulano@email.com");
		useCase.executa(dados);

		Aluno encontrado = repositorio.buscarPorCPF(new CPF("123.456.789-00"));

		assertEquals("Fulano", encontrado.getNome());
		assertEquals(new CPF("123.456.789-00"), encontrado.getCpf());
		assertEquals("fulano@email.com", encontrado.getEmail());
	}

}
