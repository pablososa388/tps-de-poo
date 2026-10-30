import java.util.ArrayList;
import java.util.List;

class EmpleadoService {
    private static List<Empleado> empleados = new ArrayList<>();
    private static int proximoLegajo = 1;

    public static Boolean agregar(Empleado empleado)
            throws EnteroPositivoException {
        empleado.setLegajo(proximoLegajo++);
        return empleados.add(empleado);
    }

    public static Empleado mayorSueldo()
            throws CollectionVaciaException {
        if (empleados.isEmpty()) {
            throw new CollectionVaciaException("No hay empleados.");
        }
        // Lógica omitida para brevedad
        return empleados.get(0);
    }

    public static Double sueldoPromedio()
            throws CollectionVaciaException {
        if (empleados.isEmpty()) {
            throw new CollectionVaciaException("No hay empleados.");
        }
        return 0.0; // Lógica omitida
    }

    public static void eliminar(String nombre)
            throws CollectionVaciaException, NoEncontradoException {
        if (empleados.isEmpty()) {
            throw new CollectionVaciaException("No hay empleados.");
        }

        boolean eliminado = empleados.removeIf(
            e -> e.getNombre().equals(nombre)
        );

        if (!eliminado) {
            throw new NoEncontradoException(
                "No se encontro el empleado."
            );
        }
    }
}