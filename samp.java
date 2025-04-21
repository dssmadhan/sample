import java.rmi.Remote;
import java.rmi.RemoteException;

public interface samp extends Remote {
    String sayhello(String name) throws RemoteException;
}