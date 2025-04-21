import java.rmi.registry.*;

public class sampserver {
    public static void main(String[] args){
        try{
            sampimple sam = new sampimple();

            Registry reg=LocateRegistry.createRegistry(1100);
            reg.rebind("Hello",sam);
            System.out.println("running server");
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
