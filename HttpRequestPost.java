import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.security.MessageDigest;
import java.util.HashMap;
import java.util.Map;

public class HttpRequestPost {
    public static void main(String[] args) {
        String urlAdress = "http://127.0.0.1:8080/file";
        URL url;
        HttpURLConnection httpURLConnection;
        OutputStream os = null;
        InputStreamReader isR = null;
        BufferedReader bfR = null;
        StringBuilder stringBuilder = new StringBuilder();
        try {
            Map<String, String> postargs = new HashMap<>();
            postargs.put("coods", "56.484119,46.958815");
            String ff= new String();

            ff = "{'coods': '56.484119,46.958815', 'text': 'Нет нормальных дорог!', 'file': 'b'sadasdasdasdas''";
            byte[] out = ff.toString().getBytes();
            System.out.print(postargs);


            url = new URL(urlAdress);
            httpURLConnection = (HttpURLConnection) url.openConnection();
            httpURLConnection.setRequestMethod("POST");
            httpURLConnection.setDoOutput(true);
            httpURLConnection.setDoInput(true);
            httpURLConnection.addRequestProperty("User-Agent", "Mozilla/5.0");
            httpURLConnection.addRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            httpURLConnection.setConnectTimeout(200);
            httpURLConnection.setReadTimeout(200);
            httpURLConnection.connect();
            try {
                os = httpURLConnection.getOutputStream();
                os.write(out);

            } catch (Exception e) {
                System.err.print(e.getMessage());
            }
            if (HttpURLConnection.HTTP_OK == httpURLConnection.getResponseCode()) ;
            {
                isR = new InputStreamReader(httpURLConnection.getInputStream());
                bfR = new BufferedReader(isR);
                String line;
                while ((line = bfR.readLine()) != null) {
                    stringBuilder.append(line);

                }
            }

System.out.print(stringBuilder);
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            System.err.print(e.getMessage());
        } finally {
            try {
                isR.close();

            } catch (IOException e) {
                e.printStackTrace();
            }
            try {
                bfR.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            try {
                os.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
