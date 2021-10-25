package com.example.iotapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import java.util.Objects;


public class MainActivity extends AppCompatActivity {


    FirebaseDatabase firebaseDatabase;

    DatabaseReference databaseReference;

    // variable for Text view.
    private TextView retrieveTV;

    private ImageView imageIV;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        firebaseDatabase = FirebaseDatabase.getInstance();
        databaseReference = firebaseDatabase.getReference("message");
        retrieveTV = findViewById(R.id.idTVRetrieveData);
        imageIV = findViewById(R.id.imageView1);
        getdata();
    }
    private void getdata() {
        // calling add value event listener method
        // for getting the values from database.
        databaseReference.addValueEventListener(new ValueEventListener() {
                @Override
                public void onDataChange(@NonNull DataSnapshot snapshot) {
                    // this method is call to get the realtime
                    // updates in the data.
                    // this method is called when the data is
                    // changed in our Firebase console.
                    // below line is for getting the data from
                    // snapshot of our database.
                    String value = snapshot.getValue(String.class);
                    String textvalue =  "You are " + value + " right now";
                    // after getting the value we are setting
                    // our value to our text view in below line.
                    retrieveTV.setText(textvalue);
                    switch (Objects.requireNonNull(value)) {
                        case "idle":
                            imageIV.setImageResource(R.drawable.idle);
                            break;
                        case "walking":
                            imageIV.setImageResource(R.drawable.walk);
                            break;
                        case "running":
                            imageIV.setImageResource(R.drawable.run);
                            break;
                        default:
                            imageIV.setImageResource(R.drawable.idle);
                            break;
                    }
                }
                @Override
                public void onCancelled(@NonNull DatabaseError error) {
                    Toast.makeText(MainActivity.this, "Fail to get data.", Toast.LENGTH_SHORT).show();
                }
            });
        }
    }
