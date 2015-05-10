class CouchUploader

  require 'net/http'
  require 'json'

  COUCH_PORT = 5984
  COUCH_IP = '144.6.227.66'

  def self.upload_documents documents, id_key = nil
    # Upload each document using id key
    documents.each do |doc|
      if id_key
        key = doc[id_key]
      else
        # Get a key from couch
        key = get_uuid
      end


      puts "key is #{key}"
      # Upload the document to couch
      http = Net::HTTP.new(COUCH_IP, COUCH_PORT)
      response = http.send_request('PUT', "/tweets/#{key}", doc.to_json)
      puts response
    end
  end

  private

  def self.get_uuid
    result = JSON.parse(Net::HTTP.get(URI.parse("http://#{COUCH_IP}:#{COUCH_PORT}/_uuids")))
    key = result["uuids"].first
  end

end
