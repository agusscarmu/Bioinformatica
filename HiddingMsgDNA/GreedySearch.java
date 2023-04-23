package HiddingMsgDNA;

import java.util.HashMap;

public class GreedySearch {
    
    public static void main (String[]args){
        String[]adn={"GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"};
        int k=3;
        int t=5;
        String[]resultado=GreedyMotifSearch(adn,k,t);
        System.out.println(resultado.toString());
    }

    public static String[] GreedyMotifSearch(String[]adn, int k, int t){
        String[] BestMotifs = new String[t];
        for(int i=0;i<t;i++){
            BestMotifs[i]=(adn[i].substring(0, k));
        }
        int n=adn[0].length();

        for(int i=0; i<n-k+1; i++){
            String[] Motif = new String[t];
            Motif[i]=(adn[0].substring(i, i+k));
            for(int j=1;j<t;j++){
                HashMap<Character, double[]> p=profile(Motif);
                Motif[j]=(MostProbableKmer(adn[j], k, p));
            }
            if(Score(Motif)<Score(BestMotifs)){
                BestMotifs=Motif;
            }
        }
        return BestMotifs;
    }

    public static int Score(String[]Motif){
        int score=0;
        HashMap<Character,double[]>count = Count(Motif);
        Character[]Nucleotidos={'A','C','G','T'};
        int sizeMotif=Motif.length;
        int t=count.get('A').length;
        for(int i=0;i<t;i++){
            int mayor=0;
            int res=0;
            for(Character n:Nucleotidos){
                double[]a=count.get(n);
                if(mayor<(int)a[i]){
                    mayor=(int)a[i];
                }
            }
            res=sizeMotif-mayor;
            score+=res;
        }
        return score;
    }
    
    public static HashMap<Character, double[]> Count(String[]Motif){
        Character[]Nucleotidos={'A','C','G','T'};
        int t=Motif[0].length();
        HashMap<Character, double[]> count=new HashMap<>();
        for(Character symbol:Nucleotidos){
            count.put(symbol, new double[t]);
        }
        int n=Motif.length;
        for(int i=0;i<n;i++){
            for(int j=0;j<t;j++){
                Character symbol = Motif[i].charAt(2);
                double[] a =count.get(symbol);
                a[j]+=1;
                count.put(symbol, a);
            }
        }
        return count;
    }

    public static HashMap<Character, double[]> profile(String[] Motif){
        HashMap<Character, double[]> salida = Count(Motif);
        int t=salida.get('A').length;
        int n=salida.size();
        Character[]Nucleotidos={'A','C','G','T'};

        for(Character symbol:Nucleotidos){
            for(int i=0;i<t;i++){
                double[]a=salida.get(symbol);
                a[i]/=n;
                salida.put(symbol, a);
            }
        }

        return salida;
    }

    public static String MostProbableKmer(String adn, int k, HashMap<Character, double[]>profile){
        String kmer="";
        int n= adn.length();
        float bestPr=0;

        for(int i=0;i<n-k+1;i++){
            String pattern = adn.substring(i, i+k);
            float Pr=Pr(pattern, profile);
            if(bestPr<Pr){
                bestPr=Pr;
                kmer=pattern;
            }
        }

        return kmer;
    }

    public static float Pr(String kmer, HashMap<Character, double[]>profile){

        int k=kmer.length();
        float Pr=1;

        for(int i=0;i<k;i++){
            char nucleotido = kmer.charAt(i);
            double[]p=profile.get(nucleotido);
            Pr*=p[i];
        }

        return Pr;
    }

}
