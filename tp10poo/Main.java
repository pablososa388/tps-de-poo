public class Main {
    public static void main(String[] args) {

        // 1. Crear empleado con sueldo inválido
        try {
            Empleado e = new Empleado("Juan", -100);
        } catch (StringException | EnteroPositivoException e) {
            System.out.println(e.getMessage());
        }

        // 2. Eliminar empleado inexistente
        try {
            EmpleadoService.eliminar("Eustaquio");
        } catch (CollectionVaciaException | NoEncontradoException e) {
            System.out.println(e.getMessage());
        }

        // 3. Calcular promedio con lista vacía
        try {
            EmpleadoService.sueldoPromedio();
        } catch (CollectionVaciaException e) {
            System.out.println(e.getMessage());
        }
        // Legajo menor a 0
        try {
            Empleado e = new Empleado("Pablo", 1000);
            e.setLegajo(-1);
        } catch (StringException | EnteroPositivoException e) {
            System.out.println(e.getMessage());
        }
    }
        
        
}