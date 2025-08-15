package com.hvitoi.tdd.service;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.math.BigDecimal;
import java.time.LocalDate;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.hvitoi.tdd.modelo.Desempenho;
import com.hvitoi.tdd.modelo.Funcionario;

public class ReajusteServiceTest {

	private ReajusteService service;
	private Funcionario fulano;

	@BeforeEach
	public void inicializar() {
		this.service = new ReajusteService();
		this.fulano = new Funcionario("Fulano", LocalDate.now(), new BigDecimal("2000.00"));
	}

	// @AfterEach
	// public void finalizar() {
	// System.out.println("fim");
	// }

	// @BeforeAll
	// public void antesDeTodos() {
	// System.out.println("antes de todos");
	// }

	// @AfterAll
	// public void depoisDeTodos() {
	// System.out.println("depois de todos");
	// }

	@Test
	void reajusteDeveriaSerDeTresPorcentoQuandoDesempenhoForADesejar() {
		service.concederReajuste(fulano, Desempenho.A_DESEJAR);

		assertEquals(new BigDecimal("2060.00"), fulano.getSalario());
	}

	@Test
	void reajusteDeveriaSerDeQuinzePorcentoQuandoDesempenhoForBom() {
		service.concederReajuste(fulano, Desempenho.BOM);

		assertEquals(new BigDecimal("2300.00"), fulano.getSalario());
	}

	@Test
	void reajusteDeveriaSerDeVintePorcentoQuandoDesempenhoForOtimo() {
		service.concederReajuste(fulano, Desempenho.OTIMO);

		assertEquals(new BigDecimal("2400.00"), fulano.getSalario());
	}

}
