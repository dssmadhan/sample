import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class sampimple extends UnicastRemoteObject implements samp{
    protected sampimple() throws RemoteException{
        super();
    }

    @Override
    public String sayhello(String name) throws RemoteException{
        return "Hello, "+name;
    }
}