using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading.Tasks;

namespace TestServer
{
    class Program
    {
        static void Main(string[] args)
        {
            // The code provided will print ‘Hello World’ to the console.
            // Press Ctrl+F5 (or go to Debug > Start Without Debugging) to run your app.
            Console.WriteLine("Hello World!");

            TcpListener server = null;
            try
            {
                int port = 6000;
                server = new TcpListener(6000);
                server.Start();

                while(true)
                {
                    Console.WriteLine("Waiting for a connection...");
                    TcpClient client = server.AcceptTcpClient();
                    Console.WriteLine("Connected");

                    NetworkStream  stream = client.GetStream();

                    String message = "You have connected to C# Server";
                    while (true)
                    {
                        Byte[] data = System.Text.Encoding.ASCII.GetBytes(message);
                        stream.Write(data, 0, data.Length);
                        Console.WriteLine("Enter message to send");
                        message = Console.ReadLine();
                        if (message == "quit")
                            break;
                    }
                    


                    stream.Close();
                    // Shutdown and end connection
                    client.Close();
                }
            }
            catch (SocketException e)
            {
                Console.WriteLine("SocketException: {0}", e);
            }
            finally
            {
                // Stop listening for new clients.
                server.Stop();
            }


            Console.WriteLine("\nHit enter to continue...");
            Console.Read();
        }



    }
      
}
