package HiddingMsgDNA;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Count {
    
    public static void main(String[]args){
        List<String> Motif= Arrays.asList(
            "TCGGGGGTTTTT",
            "CCGGTGACTTAC",
            "ACGGGGATTTTC",
            "TTGGGGACTTTT",
            "AAGGGGACTTCC",
            "TTGGGGACTTCC",
            "TCGGGGATTCAT",
            "TCGGGGATTCCT",
            "TAGGGGAACTAC",
            "TCGGGTATAACC"
            );
        System.out.println(Profile(Motif));    

    }

    public static Map<String, List<Integer>> Profile(List<String> Motif){

        Map<String, List<Integer>> salida = new HashMap<>();

        List<String> nucleotido= Arrays.asList("A","C","G","T");

        int t=Motif.size();
        int k=Motif.get(0).length();

        for(String symbol:nucleotido){
            List<Integer> lista=new ArrayList<>(Collections.nCopies(k, 0));
            salida.put(symbol, lista);
        }

        for(int i=0;i<t;i++){
            for(int j=0;j<k;j++){
                char symbol = Motif.get(i).charAt(j);
                String s = new String(symbol+"");
                Integer valorActual=salida.get(s).get(j);
                Integer valorNuevo=valorActual+1;
                salida.get(s).add(valorNuevo++);
            }
        }
        return salida;
    }
    
}
