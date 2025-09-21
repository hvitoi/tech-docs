import java.math.BigDecimal;

class Main {
  public static void main(String[] args) {

  }
}

enum StatusTopico {
  NAO_RESPONDIDO, NAO_SOLUCIONADO, SOLUCIONADO, FECHADO
}

// "Strategy" Design Pattern
enum Desempenho {
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
