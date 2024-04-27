package com.hvitoi.escola.gamificacao.aplicacao;

import com.hvitoi.escola.gamificacao.dominio.selo.RepositorioDeSelos;
import com.hvitoi.escola.gamificacao.dominio.selo.Selo;
import com.hvitoi.escola.shared.dominio.CPF;
import com.hvitoi.escola.shared.dominio.evento.Evento;
import com.hvitoi.escola.shared.dominio.evento.Ouvinte;
import com.hvitoi.escola.shared.dominio.evento.TipoDeEvento;

public class GeraSeloAlunoNovato extends Ouvinte {

	private final RepositorioDeSelos repositorioDeSelos;

	public GeraSeloAlunoNovato(RepositorioDeSelos repositorioDeSelos) {
		this.repositorioDeSelos = repositorioDeSelos;
	}

	@Override
	protected void reageAo(Evento evento) {
		CPF cpfDoAluno = (CPF) evento.informacoes().get("cpf");
		Selo novato = new Selo(cpfDoAluno, "Novato");
		repositorioDeSelos.adicionar(novato);
	}

	@Override
	protected boolean deveProcessar(Evento evento) {
		return evento.tipo() == TipoDeEvento.ALUNO_MATRICULADO;
	}

}
