package com.hvitoi.tdd.service;

import java.math.BigDecimal;

import com.hvitoi.tdd.modelo.Desempenho;
import com.hvitoi.tdd.modelo.Funcionario;

public class ReajusteService {

	public void concederReajuste(Funcionario funcionario, Desempenho desempenho) {
		BigDecimal reajuste = desempenho.percentualReajuste(); // "Strategy" Design Pattern
		funcionario.reajustarSalario(reajuste);
	}

}
