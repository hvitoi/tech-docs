package com.hvitoi.escola.gamificacao.dominio.selo;

import java.util.List;

import com.hvitoi.escola.shared.dominio.CPF;

public interface RepositorioDeSelos {

	void adicionar(Selo selo);

	List<Selo> selosDoAlunoDeCPF(CPF cpf);

}
