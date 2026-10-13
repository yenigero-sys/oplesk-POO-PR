class DispensadorDeTurnos:
    def __init__(self):
        self.ultimo_turno_dado = 0
        self.turno_atendiendo = 0

    def tomar_turno(self) -> int:
        """
        Toma un turno para el banco e imprime en consola el estatus actual.

        Returns:
            int -> El último turno dado.
        """
        self.ultimo_turno_dado += 1
        pendientes = self.ultimo_turno_dado - self.turno_atendiendo
        print(f"Turno emitido: {self.ultimo_turno_dado} | Personas en espera: {pendientes}")
        return self.ultimo_turno_dado

    def llamar_siguiente(self) -> None:
        """Llama al siguiente turno en la fila."""
        if self.turno_atendiendo < self.ultimo_turno_dado:
            self.turno_atendiendo += 1
            print(f"- Llamando al turno: {self.turno_atendiendo}")
        else:
            print("No hay clientes esperando en la fila.")


def main() -> None:
    banco = DispensadorTurnos()

    banco.tomar_turno()  # llama al primer cliente del banco
    banco.tomar_turno()  # llama al segundo
    banco.tomar_turno()  # llama al tercero

    banco.llamar_siguiente()  # Juan
    banco.llamar_siguiente()  # Ana


    banco.tomar_turno()  # Pablo (turno 4)

    banco.llamar_siguiente()
    banco.llamar_siguiente()

    banco.llamar_siguiente()


if __name__ == "__main__":
    main()
