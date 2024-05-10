package com.hvitoi.escola.academico.dominio.aluno;

import java.util.List;

import com.hvitoi.escola.shared.dominio.CPF;

public interface RepositorioDeAlunos {

	void matricular(Aluno aluno);

	Aluno buscarPorCPF(CPF cpf);

	List<Aluno> listarTodosAlunosMatriculados();

	// ...

}
