package com.hvitoi.escola.dominio.aluno;

public class FabricaDeAluno {

	private Aluno aluno;

	public FabricaDeAluno comNomeCPFEmail(String nome, String cpf, String email) {
		this.aluno = new Aluno(new CPF(cpf), nome, new Email(email));
		return this; // returns the factory itself
	}

	public FabricaDeAluno comTelefone(String ddd, String numero) {
		this.aluno.adicionarTelefone(ddd, numero);
		return this;
	}

	public Aluno criar() { // .build
		return this.aluno;
	}

}
