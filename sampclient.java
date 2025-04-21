import java.rmi.registry.*;

public class sampclient {
    public static void main(String[] args){
        try{
            Registry reg=LocateRegistry.getRegistry("localhost",1100);
            samp sam=(samp)reg.lookup("Hello");
            String res=sam.sayhello("Vijay");
            System.out.println(res);

        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
