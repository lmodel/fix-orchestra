package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  This is the default type for all of the DC elements. It permits text content only with optional xml:lang attribute. Text is allowed because mixed="true", but sub-elements are disallowed because minOccurs="0" and maxOccurs="0" are on the xs:any tag. This complexType allows for restriction or extension permitting child elements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DcSimpleLiteral  {

  private String value;
  private List<String> content;
  private String lang;


}