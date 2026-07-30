package com.example.productmanagement;

import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private TextView tvScannedId;
    private TextView tvProductInfo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvScannedId = findViewById(R.id.tvScannedId);
        tvProductInfo = findViewById(R.id.tvProductInfo);

        // Initial setup for scanner connection
        tvScannedId.setText("Scanned ID: 123456789");
        tvProductInfo.setText("Code: Sample Product A\nFile: TR11122\nDatabase: Main DB\nStatus: Validated - Product in Database");
    }
}
