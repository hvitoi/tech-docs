package com.hvitoi.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import com.hvitoi.modelo.Topico;

public interface TopicoRepository extends JpaRepository<Topico, Long> {

	// topico.curso.nome (findByCurso_Nome)
	List<Topico> findByCursoNome(String nomeCurso);

	// mesma coisa, mas com uma nova assinatura
	// @Query("SELECT t FROM Topico t WHERE t.curso.nome = :nomeCurso")
	// List<Topico> carregarPorNomeDoCurso(@Param("nomeCurso") String nomeCurso);

}
