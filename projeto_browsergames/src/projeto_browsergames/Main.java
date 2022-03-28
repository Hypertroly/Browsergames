package projeto_browsergames;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;

public class Main{
	

	public static void main(String[] args) {
		String dbURL = "jdbc:mysql://localhost:3306/browsergames";
		String username = "root";
		String password = "browsergame";
		 
		try {
		 
		    Connection conn = DriverManager.getConnection(dbURL, username, password);
		    String sql = "INSERT INTO categoria (nome) VALUES (?)";
		    
		    PreparedStatement statement = conn.prepareStatement(sql);
		    statement.setString(1, "Aventura");
		     
		    int rowsInserted = statement.executeUpdate();
		    if (rowsInserted > 0) {
		        System.out.println("A nova categoria foi inserida com sucesso");
		    }
		    conn.close();
		    if (conn != null) {
		        System.out.println("Connected");
		    }
		} catch (SQLException ex) {
		    ex.printStackTrace();
		    }
		}
}