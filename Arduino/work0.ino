/*--------------------------------------------------------
第0回
for(int i=0;i<6;i++) を使って、ループ処理中のiの値を表示し、
1秒間待機するプログラムを作ってください。
--------------------------------------------------------*/

void setup() {
    Serial.begin(9600); // シリアルポートを9600bpsで開く
}

void loop() {
        for(int i=0;i<6;i++){
        Serial.println("Hello World")
        delay(100)
    }
}