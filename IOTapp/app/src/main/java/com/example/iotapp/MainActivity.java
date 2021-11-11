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
    DatabaseReference databaseReference1;
    DatabaseReference databaseReference2;
    DatabaseReference databaseReference3;


    // variable for Text view.
    private TextView retrieveTV;
    private ImageView imageIV;
    private TextView count1;
    private TextView count2;
    private TextView count3;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        firebaseDatabase = FirebaseDatabase.getInstance();
        databaseReference = firebaseDatabase.getReference("message");
        databaseReference1 = firebaseDatabase.getReference("pushup_count");
        databaseReference2 = firebaseDatabase.getReference("situp_count");
        databaseReference3 = firebaseDatabase.getReference("jump_count");

//        retrieveTV = findViewById(R.id.idTVRetrieveData);
//        imageIV = findViewById(R.id.imageView1);
//        count1 = findViewById(R.id.idTVcount1);
//        count2 = findViewById(R.id.idTVcount2);
//        count3 = findViewById(R.id.idTVcount3);
//        getdata();
    }
//    private void getdata() {
//        // calling add value event listener method
//        // for getting the values from database.
//        databaseReference.addValueEventListener(new ValueEventListener() {
//                @Override
//                public void onDataChange(@NonNull DataSnapshot snapshot) {
//                    // this method is call to get the realtime
//                    // updates in the data.
//                    // this method is called when the data is
//                    // changed in our Firebase console.
//                    // below line is for getting the data from
//                    // snapshot of our database.
//                    String value = snapshot.getValue(String.class);
//                    String textvalue =  "Current Activity: " + value;
//                    // after getting the value we are setting
//                    // our value to our text view in below line.
//                    retrieveTV.setText(textvalue);
//                    switch (Objects.requireNonNull(value)) {
//                        case "idle":
//                            imageIV.setImageResource(R.drawable.idle);
//                            break;
//                        case "walking":
//                            imageIV.setImageResource(R.drawable.walk);
//                            break;
//                        case "running":
//                            imageIV.setImageResource(R.drawable.run);
//                            break;
//
//                        case "push-up":
//                            imageIV.setImageResource(R.drawable.pushup);
//                            break;
//
//                        case "sit-up":
//                            imageIV.setImageResource(R.drawable.situp);
//                            break;
//
//                        case "jumping jack":
//                            imageIV.setImageResource(R.drawable.jump);
//                            break;
//                        default:
//                            imageIV.setImageResource(R.drawable.idle);
//                            break;
//                    }
//                }
//                @Override
//                public void onCancelled(@NonNull DatabaseError error) {
//                    Toast.makeText(MainActivity.this, "Fail to get data.", Toast.LENGTH_SHORT).show();
//                }
//            });
//
//        databaseReference1.addValueEventListener(new ValueEventListener() {
//            @Override
//            public void onDataChange(@NonNull DataSnapshot snapshot) {
//                // this method is call to get the realtime
//                // updates in the data.
//                // this method is called when the data is
//                // changed in our Firebase console.
//                // below line is for getting the data from
//                // snapshot of our database.
//                Integer value = snapshot.getValue(Integer.class);
//                String textvalue =  String.valueOf(value) + " Reps";
//                // after getting the value we are setting
//                // our value to our text view in below line.
//                count1.setText(textvalue);
//            }
//            @Override
//            public void onCancelled(@NonNull DatabaseError error) {
//                Toast.makeText(MainActivity.this, "Fail to get data.", Toast.LENGTH_SHORT).show();
//            }
//        });
//
//        databaseReference2.addValueEventListener(new ValueEventListener() {
//            @Override
//            public void onDataChange(@NonNull DataSnapshot snapshot) {
//                // this method is call to get the realtime
//                // updates in the data.
//                // this method is called when the data is
//                // changed in our Firebase console.
//                // below line is for getting the data from
//                // snapshot of our database.
//                Integer value = snapshot.getValue(Integer.class);
//                String textvalue =  String.valueOf(value) + " Reps";
//                // after getting the value we are setting
//                // our value to our text view in below line.
//                count2.setText(textvalue);
//            }
//            @Override
//            public void onCancelled(@NonNull DatabaseError error) {
//                Toast.makeText(MainActivity.this, "Fail to get data.", Toast.LENGTH_SHORT).show();
//            }
//        });
//
//        databaseReference3.addValueEventListener(new ValueEventListener() {
//            @Override
//            public void onDataChange(@NonNull DataSnapshot snapshot) {
//                // this method is call to get the realtime
//                // updates in the data.
//                // this method is called when the data is
//                // changed in our Firebase console.
//                // below line is for getting the data from
//                // snapshot of our database.
//                Integer value = snapshot.getValue(Integer.class);
//                String textvalue =  value + " Reps";
//                // after getting the value we are setting
//                // our value to our text view in below line.
//                count3.setText(textvalue);
//            }
//            @Override
//            public void onCancelled(@NonNull DatabaseError error) {
//                Toast.makeText(MainActivity.this, "Fail to get data.", Toast.LENGTH_SHORT).show();
//            }
//        });
//        }
    }
