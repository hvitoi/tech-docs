package com.hvitoi.tdd.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

import java.math.BigDecimal;
import java.time.LocalDate;

import com.hvitoi.tdd.modelo.Funcionario;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class BonusServiceTest {

	private BonusService service;

	@BeforeEach
	public void inicializa() {
		this.service = new BonusService();
	}

	@Test
	void bonusDeveriaSerZeroParaFuncionarioComSalarioMuitoAlto() {

		// assertThrows(//
		// IllegalArgumentException.class, //
		// () -> service.calcularBonus(criarFuncionario(new BigDecimal("25000"))) //
		// );

		try {
			service.calcularBonus(criarFuncionario(new BigDecimal("25000")));
			fail("nao deu exception"); // fails if the code does not throw exception
		} catch (IllegalArgumentException e) {
			// good approach when you need to analyze the exception message
			assertEquals("Funcionario com salario maior do que R$1000 nao pode receber bonus!", e.getMessage());
		}

	}

	@Test
	void bonusDeveriaSer10PorCentoDoSalario() {
		BigDecimal bonus = service.calcularBonus(criarFuncionario(new BigDecimal("2500")));

		assertEquals(new BigDecimal("250.00"), bonus);
	}

	@Test
	void bonusDeveriaSerDezPorCentoParaSalarioDeExatamente10000() {
		BigDecimal bonus = service.calcularBonus(criarFuncionario(new BigDecimal("10000")));

		assertEquals(new BigDecimal("1000.00"), bonus);
	}

	private Funcionario criarFuncionario(BigDecimal salario) {
		return new Funcionario("Rodrigo", LocalDate.now(), salario);
	}

}
