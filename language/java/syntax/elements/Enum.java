import java.math.BigDecimal;

enum StatusTopico {
  NAO_RESPONDIDO, NAO_SOLUCIONADO, SOLUCIONADO, FECHADO
}

// "Strategy" Design Pattern
public enum Desempenho {
  A_DESEJAR {
    @Override
    public BigDecimal percentualReajuste() {
      return new BigDecimal("0.03");
    }
  },
  BOM {
    @Override
    public BigDecimal percentualReajuste() {
      return new BigDecimal("0.15");
    }
  },
  OTIMO {
    @Override
    public BigDecimal percentualReajuste() {
      return new BigDecimal("0.20");
    }
  };

  public abstract BigDecimal percentualReajuste();

}
